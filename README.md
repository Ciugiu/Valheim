# Valheim Server Setup

Configuration files and setup for hosting a Valheim dedicated server using Docker. This repository contains everything needed to quickly deploy and manage a Valheim server for you and your friends.

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

#### Discord Integration
- `DISCORD_WEBHOOK` - Discord webhook URL for server notifications
- `PLAYER_JOIN_MESSAGE` - Custom message when players join
- `BACKUP_NOTIFICATION_MESSAGE` - Custom message for backup notifications

### Example Configuration

```env
SERVER_NAME=Viking Warriors
WORLD_NAME=Midgard
SERVER_PASS=super_secret_password

SUPERVISOR_USER=admin
SUPERVISOR_PASS=admin_password

DISCORD_WEBHOOK=https://discord.com/api/webhooks/your/webhook/url
PLAYER_JOIN_MESSAGE=A Viking has joined the server!
BACKUP_NOTIFICATION_MESSAGE=World backup completed successfully
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
└── README.md            # This file
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
Navigate to `http://your-server-ip:9001` and log in with your supervisor credentials.

## 🎮 Connecting to Your Server

1. Launch Valheim
2. Go to "Join Game"
3. Click "Add Server"
4. Enter your server IP and port
5. Enter the server password you configured

## 🔒 Security Notes

- Never commit your `.env` file to version control (it's in `.gitignore`)
- Use strong passwords for both server access and supervisor interface
- Consider using a firewall to restrict access to necessary ports only
- Keep your Discord webhook URL private

## 🤝 Contributing

Feel free to submit issues and enhancement requests!

## 📜 License

This project is open source and available under the [MIT License](LICENSE).

## 🙋‍♂️ Support

If you encounter any issues or have questions about the setup, please open an issue in this repository.

---

**Happy Viking adventures! ⚔️🛡️**
