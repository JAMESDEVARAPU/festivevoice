# Deployment Guide

This guide covers different deployment options for the Indian Cultural Heritage Collection Platform.

## 📋 Prerequisites

- Python 3.8 or higher
- Git
- API keys for OpenAI and Anthropic (optional but recommended)

## 🚀 Deployment Options

### 1. Local Development

**Quick Start:**
```bash
git clone <repository-url>
cd indian-cultural-heritage-platform
pip install streamlit pandas anthropic openai
streamlit run app.py --server.port 5000
```

### 2. Replit Deployment

1. **Import Repository**
   - Go to Replit and create a new Repl
   - Choose "Import from GitHub" and paste your GitLab repository URL
   - Replit will automatically detect it's a Python project

2. **Configure Environment**
   - Add secrets in the Secrets tab:
     - `OPENAI_API_KEY`: Your OpenAI API key
     - `ANTHROPIC_API_KEY`: Your Anthropic API key

3. **Run the Application**
   - The application will automatically start with the configured workflow
   - Access via the provided Replit URL

### 3. Heroku Deployment

1. **Prepare Files**
   Create `Procfile`:
   ```
   web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
   ```

2. **Deploy**
   ```bash
   heroku create your-app-name
   heroku config:set OPENAI_API_KEY=your_key
   heroku config:set ANTHROPIC_API_KEY=your_key
   git push heroku main
   ```

### 4. Streamlit Cloud

1. **Connect Repository**
   - Go to share.streamlit.io
   - Connect your GitLab repository
   - Select the main branch and app.py

2. **Configure Secrets**
   - Add secrets in the app settings:
     - `OPENAI_API_KEY`
     - `ANTHROPIC_API_KEY`

### 5. Docker Deployment

1. **Create Dockerfile**
   ```dockerfile
   FROM python:3.9-slim
   
   WORKDIR /app
   COPY . .
   
   RUN pip install streamlit pandas anthropic openai
   
   EXPOSE 8501
   
   ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
   ```

2. **Build and Run**
   ```bash
   docker build -t cultural-heritage-app .
   docker run -p 8501:8501 cultural-heritage-app
   ```

## 🔐 Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `OPENAI_API_KEY` | OpenAI API key for content validation | Optional |
| `ANTHROPIC_API_KEY` | Anthropic API key for content validation | Optional |

## 📊 Performance Considerations

### Resource Requirements
- **Minimum**: 512MB RAM, 1 CPU core
- **Recommended**: 1GB RAM, 2 CPU cores
- **Storage**: 100MB + user uploads

### Optimization Tips
- Enable caching for large data operations
- Use lazy loading for multimedia content
- Implement pagination for large datasets
- Monitor API usage and implement rate limiting

## 🔒 Security Best Practices

### API Keys
- Never commit API keys to version control
- Use environment variables or secrets management
- Rotate keys regularly
- Monitor API usage for anomalies

### User Data
- Implement proper authentication
- Sanitize user inputs
- Regular security audits
- Backup user data regularly

## 📈 Monitoring and Maintenance

### Health Checks
- Monitor application uptime
- Check API response times
- Monitor storage usage
- Track user engagement metrics

### Regular Maintenance
- Update dependencies monthly
- Backup data weekly
- Review and update documentation
- Monitor for security vulnerabilities

## 🆘 Troubleshooting

### Common Issues

**Port Already in Use**
```bash
# Kill process using port 5000
lsof -ti:5000 | xargs kill -9
```

**Missing Dependencies**
```bash
# Reinstall dependencies
pip install --force-reinstall streamlit pandas anthropic openai
```

**API Key Issues**
- Verify keys are correctly set in environment
- Check API quotas and billing
- Test with minimal API calls

### Log Analysis
- Check Streamlit logs for errors
- Monitor API call logs
- Review user activity logs

## 📞 Support

For deployment issues:
1. Check this documentation first
2. Review application logs
3. Create an issue with deployment details
4. Contact the development team

---

**Note**: This platform preserves cultural heritage - please ensure reliable deployment for community access.