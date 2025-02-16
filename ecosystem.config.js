module.exports = {
  apps: [
    {
      name: 'django-api',
      script: '/home/jarbas/.virtualenvs/django-env/bin/gunicorn', // Caminho absoluto para o gunicorn no ambiente virtual
      args: 'config.wsgi:application --bind 0.0.0.0:8000 --workers 3',
      exec_mode: 'fork',
      autorestart: true,
      watch: false,
      max_memory_restart: '1G',
      env: {
        DJANGO_SETTINGS_MODULE: 'config.settings',
        ENV: 'development',
      },
      env_production: {
        DJANGO_SETTINGS_MODULE: 'config.settings',
        ENV: 'production',
      },
    },
  ],

  deploy: {
    production: {
      user: 'jarbas',
      host: 'smartmonitor.ifce.edu.br',
      ref: 'origin/main',
      repo: 'https://github.com/douglasnobree/SmartMonitorAPI.git',
      path: '/home/jarbas/iot-django',
      'post-deploy':
        'export PATH=$PATH:/home/jarbas/.nvm/versions/node/v20.18.1/bin && source /home/jarbas/.virtualenvs/django-env/bin/activate && pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --noinput && pm2 reload ecosystem.config.js --env production',
    },
  },
};
