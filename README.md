# Microservice Registration in Python Flask

## Usage

### How to register a microservice to CT

```python
import CTRegisterMicroserviceFlask

info = load_config_json('register')
swagger = load_config_json('swagger')
CTRegisterMicroserviceFlask.register(
    app = application,
    name = '<microservice_name>',
    info = info,
    swagger = swagger,
    mode = CTRegisterMicroserviceFlask.AUTOREGISTER_MODE if os.getenv('ENVIRONMENT') == 'dev' else CTRegisterMicroserviceFlask.NORMAL_MODE,
    ct_url = os.getenv('CT_URL'),
    url = os.getenv('LOCAL_URL')
)
```

### How to do a request to another microservice

```python
import CTRegisterMicroserviceFlask

config = {
    'uri': '/dataset/d02df2f6-d80c-4274-bb6f-f062061655c4',
    'method': 'GET',
}
response = CTRegisterMicroserviceFlask.request_to_microservice(config)
```
