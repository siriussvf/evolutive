(function () {
  const recBtn = document.querySelector("[data-rec]");
  const stopBtn = document.querySelector("[data-stop]");
  const resetBtn = document.querySelector("[data-reset]");
  const statusEl = document.querySelector("[data-status]");
  const transcriptEl = document.querySelector("[data-transcript]");
  const responseEl = document.querySelector("[data-response]");
  const audioEl = document.querySelector("[data-audio]");

  if (!recBtn || !stopBtn) return;

  let mediaRecorder = null;
  let chunks = [];

  function setStatus(t) { if (statusEl) statusEl.textContent = t; }
  function setButtons(recording) { recBtn.disabled = recording; stopBtn.disabled = !recording; }

  async function startRecording() {
    chunks = [];
    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
    mediaRecorder = new MediaRecorder(stream);

    mediaRecorder.ondataavailable = (e) => { if (e.data && e.data.size > 0) chunks.push(e.data); };

    mediaRecorder.onstop = async () => {
      try {
        setStatus("Subiendo audio…");
        const blob = new Blob(chunks, { type: "audio/webm" });
        const fd = new FormData();
        fd.append("audio", blob, "input.webm");

        const r = await fetch("/process", { method: "POST", body: fd });
        const j = await r.json();

        if (!r.ok) {
          setStatus("Error en /process");
          if (responseEl) responseEl.textContent = j.error || "Error";
          return;
        }

        if (transcriptEl) transcriptEl.textContent = j.transcript || "";
        if (responseEl) responseEl.textContent = j.response || "";

        if (audioEl && j.audio_url) {
          audioEl.src = j.audio_url;
          audioEl.load();
          audioEl.play().catch(() => {});
        }

        setStatus("Listo ✅");
      } catch (e) {
        setStatus("Error procesando");
        if (responseEl) responseEl.textContent = String(e);
      } finally {
        setButtons(false);
      }
    };

    mediaRecorder.start();
    setButtons(true);
    setStatus("Grabando…");
  }

  function stopRecording() {
    if (!mediaRecorder) return;
    try {
      mediaRecorder.stop();
      const tracks = mediaRecorder.stream?.getTracks?.() || [];
      tracks.forEach((t) => t.stop());
    } catch (_) {}
    setStatus("Procesando…");
  }

  function resetChat() {
    if (transcriptEl) transcriptEl.textContent = "";
    if (responseEl) responseEl.textContent = "";
    if (audioEl) {
      audioEl.pause();
      audioEl.removeAttribute("src");
      audioEl.load();
    }
    setStatus("Listo para grabar");
  }

  recBtn.addEventListener("click", () => {
    startRecording().catch((e) => {
      setStatus("Permiso de micro denegado");
      if (responseEl) responseEl.textContent = String(e);
      setButtons(false);
    });
  });

  stopBtn.addEventListener("click", stopRecording);
  if (resetBtn) resetBtn.addEventListener("click", resetChat);

  setButtons(false);
  setStatus("Listo para grabar");
})();