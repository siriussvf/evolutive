# iE Deployment & Sovereignty Guide 🌍🏺🔓

This guide explains how to deploy **Inteligencia Evolutiva** (iE) on a global server (VPS) while keeping your data sovereign and connecting to your local AI hardware.

## 1. Global Presence: VPS Setup

To access iE from your iPhone anywhere in the world, you need a public endpoint.

### Recommended Infrastructure
- **Server**: Ubuntu 22.04+ (2GB RAM minimum for the Flask app).
- **Web Server**: Nginx (Reverse Proxy).
- **App Server**: Gunicorn.

Antes de clonar en un servidor, necesitas subir tu código a **tu propio repositorio** (GitHub, GitLab, etc.).

### A. Preparar tu Repositorio (En tu Mac)
Si aún no has subido el código a GitHub:
1. Crea un repositorio vacío en GitHub llamado `inteligencia-evolutiva`.
2. En la terminal de tu Mac, dentro de la carpeta del proyecto:
```bash
   git init
   git add .
   git commit -m "iE: Evolución Inicial"
   git branch -M main
   git remote add origin https://github.com/TU_USUARIO/inteligencia-evolutiva.git
   git push -u origin main
```

### B. Clonar en el VPS (Servidor)
Ahora sí, en tu servidor Ubuntu:
```bash
# Cambia TU_USUARIO por tu nombre de cuenta de GitHub
git clone https://github.com/TU_USUARIO/inteligencia-evolutiva.git
cd inteligencia-evolutiva
```

# 2. Setup environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 3. Running with Gunicorn (Production)
gunicorn --workers 4 --bind 0.0.0.0:5001 src.app_flask:app
```

## 2. Remote Brain: Connecting to your Home AI

Since you have powerful hardware at home (LM Studio), you don't need to pay for expensive GPU servers. Use a **Secure Tunnel**.

### Method A: Tailscale (Easiest)
1. Install **Tailscale** on both the VPS and your Home PC.
2. In the VPS `.env` file, set `LM_STUDIO_URL` to the Tailscale IP of your Home PC.
   ```env
   LM_STUDIO_URL=http://[TAILSCALE_IP]:1234/v1/chat/completions
   ```
3. Ensure LM Studio is listening on "All Interfaces" (0.0.0.0).

### Method B: Cloudflare Tunnel
1. setup a `cloudflared` tunnel on your Home PC pointing to port 1234.
2. Use the generated `your-brain.xxx.com` URL in the VPS config.

## 3. PWA Installation (Mobile)

### iPhone (iOS Safari)
1. Navigate to your global URL in **Safari**.
2. Tap the **Share** button (box with upward arrow).
3. Scroll down and tap **Add to Home Screen**.
4. iE will now behave like a native app, without browser bars.

### Android (Chrome)
1. Tap the three dots menu.
2. Select **Install App**.

## 4. Sovereignty Checklist
- [ ] **Private DB**: Use the `ievolutiva.db` (SQLite) located only on YOUR server.
- [ ] **Local LLM**: Never send data to OpenAI/Claude. Always route through your LM Studio.
- [ ] **No Analytics**: iE does not use external tracking scripts (Google Analytics, etc.).
