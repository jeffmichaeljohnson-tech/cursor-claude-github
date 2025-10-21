# Cursor × Claude × GitHub Integration

## Quick Start

1. Configure environment:
```
   cp .env.example .env
   nano .env
```

2. Generate webhook secret:
```
   openssl rand -hex 32
```

3. Start services:
```
   docker-compose up -d
```

4. Check health:
```
   curl http://localhost:8000/health
```

## Next Steps

- Configure GitHub webhook to point to your service
- Monitor logs: `docker-compose logs -f`
