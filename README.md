# Valheim Server Setup

Configuration files and setup for hosting a Valheim dedicated server using Docker. This repository contains everything needed to quickly deploy and manage a Valheim server for you and your friends, including a Telegram bot for remote server management.

> **Note:** This setup is based on the excellent [lloesche/valheim-server-docker](https://github.com/lloesche/valheim-server-docker) project, which provides a comprehensive Valheim dedicated server with automatic updates, world backup, BepInEx and ValheimPlus mod support.

## 📋 Prerequisites

- Docker
- Docker Compose
- Basic knowledge of environment variables

## 🚀 Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/Ciugiu/Valheim.git
   cd Valheim
   ```

2. **Set up environment variables**
   ```bash
   cp .env-sample .env
   ```

3. **Configure your server** (edit `.env` file)
   ```bash
   nano .env
   ```

4. **Start the server**
   ```bash
   docker-compose up -d
   ```

## ⚙️ Configuration

### Environment Variables

Copy `.env-sample` to `.env` and configure the following variables:

#### Server Settings
- `SERVER_NAME` - The name of your Valheim server (visible in server browser)
- `WORLD_NAME` - The name of your world save file
- `SERVER_PASS` - Password required to join the server

#### Supervisor Settings
- `SUPERVISOR_USER` - Username for the supervisor web interface
- `SUPERVISOR_PASS` - Password for the supervisor web interface

### Example Configuration

```env
SERVER_NAME=Viking Warriors
WORLD_NAME=Midgard
SERVER_PASS=super_secret_password

SUPERVISOR_USER=admin
SUPERVISOR_PASS=admin_password
```

## 🐳 Docker Compose

The `docker-compose.yml` file includes:
- Valheim dedicated server container
- Supervisor for process management
- Volume mounts for persistent world data
- Network configuration for multiplayer connectivity

## 📁 File Structure

```
.
├── .env-sample          # Template for environment variables
├── .gitignore           # Git ignore rules
├── docker-compose.yml   # Docker Compose configuration
├── README.md            # This file
└── TelegramBot/         # Telegram bot for remote server management
    ├── .env-sample      # Template for bot environment variables
    ├── .gitignore       # Git ignore rules for bot
    ├── Dockerfile       # Docker build configuration
    ├── docker-compose.yml  # Bot Docker Compose configuration
    ├── requirements.txt # Python dependencies
    └── valheim_api.py   # Bot and API implementation
```

## 🔧 Server Management

### Starting the Server
```bash
docker-compose up -d
```

### Stopping the Server
```bash
docker-compose down
```

### Viewing Logs
```bash
docker-compose logs -f
```

### Accessing Supervisor
Navigate to `http://your-server-ip:27000` and log in with your supervisor credentials.

## 🤖 Telegram Bot (Optional)

The `TelegramBot` directory contains a Telegram bot that allows you to remotely manage your Valheim server. It provides a FastAPI endpoint and Telegram bot interface for starting, stopping, and checking the status of your server.

### Bot Features
- `/start` - Start the Valheim server
- `/stop` - Stop the Valheim server
- `/status` - Check if the server is running

### Bot Setup

1. **Navigate to the TelegramBot directory**
   ```bash
   cd TelegramBot
   ```

2. **Set up environment variables**
   ```bash
   cp .env-sample .env
   ```

3. **Configure the bot** (edit `.env` file)
   ```bash
   nano .env
   ```

4. **Start the bot**
   ```bash
   docker-compose up -d
   ```

### Bot Environment Variables

- `BOT_TOKEN` - Your Telegram bot token (from [@BotFather](https://t.me/BotFather))
- `NGROK_URL` - Your ngrok URL for webhook communication
- `VALHEIM_DIR` - Path to the Valheim docker-compose.yml directory
- `ALLOWED_IDS` - Comma-separated list of Telegram user IDs allowed to control the server
- `NGROK_AUTHTOKEN` - Your ngrok authentication token
- `NGROK_DOMAIN` - Your ngrok domain name

### Bot Example Configuration

```env
BOT_TOKEN=123456:ABCDEF...
NGROK_URL=https://your-ngrok-subdomain.ngrok.io
VALHEIM_DIR=/path/to/Valheim/
ALLOWED_IDS=123456789,987654321
NGROK_AUTHTOKEN=your_ngrok_authtoken
NGROK_DOMAIN=your-chosen-name.ngrok.io
```

## 🎮 Connecting to Your Server

1. Launch Valheim
2. Go to "Join Game"
3. Click "Add Server"
4. Enter your server IP and port (default: 2456)
5. Enter the server password you configured

## 🔒 Security Notes

- Never commit your `.env` file to version control (it's in `.gitignore`)
- Use strong passwords for both server access and supervisor interface
- Consider using a firewall to restrict access to necessary ports only
- Keep your Telegram bot token and ngrok credentials private
- Only add trusted Telegram user IDs to the `ALLOWED_IDS` list

## 🤝 Contributing

Feel free to submit issues and enhancement requests!

## 📜 License

This project is open source and available under the [MIT License](LICENSE).

## 🙋‍♂️ Support

If you encounter any issues or have questions about the setup, please open an issue in this repository.

---

**Happy Viking adventures! ⚔️🛡️**
