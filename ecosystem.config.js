module.exports = {
  apps: [
    {
      name: 'django-api',
      script: '/home/jarbas/.virtualenvs/django-env/bin/gunicorn', // Caminho absoluto para o gunicorn no ambiente virtual
      args: 'projectSM.wsgi:application --bind 0.0.0.0:8000 --workers 3 --pythonpath /home/jarbas/iot-django/source',
      exec_mode: 'fork',
      autorestart: true,
      watch: false,
      max_memory_restart: '1G',
      env: {
        DJANGO_SETTINGS_MODULE: 'projectSM.settings', // Ajustado para refletir o nome correto do módulo de configurações
        ENV: 'development',
      },
      env_production: {
        DJANGO_SETTINGS_MODULE: 'projectSM.settings', // Ajustado para refletir o nome correto do módulo de configurações
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
        'export PATH=$PATH:/home/jarbas/.nvm/versions/node/v20.18.1/bin:/home/jarbas/.virtualenvs/django-env/bin && source /home/jarbas/.virtualenvs/django-env/bin/activate && pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --noinput && /home/jarbas/.nvm/versions/node/v20.18.1/bin/pm2 reload ecosystem.config.js --env production',
    },
  },
};
