#Launch the application using gunicorn backend
#gunicorn -w 4 -b 0.0.0.0:${APP_ENDPOINT_PORT:-8045} app.main:app
#  --preload 
gunicorn -w 4 -k uvicorn.workers.UvicornWorker -b 0.0.0.0:${API_ENDPOINT_PORT:-8000} --log-level ${LOG_VERBOSITY:-INFO} --timeout 300 app.main:app
#--log-level ${APP_VERBOSITY:-INFO}
#python ./app/main.py