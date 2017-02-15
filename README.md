# Microservice Registration in Python Flask

## Usage

### How to register a microservice to CT

```python
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
config = {
    'uri': '/dataset/12332-123123-123123-11111',
    'method': 'GET',
}
response = request_to_microservice(config)
```
