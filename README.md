## Pasos para ejecutar el codigo correctamente


### Clonar
```
git clone https://github.com/SonicWD/Back-Inventarios.git
```

### Entrar en la carpeta
```
cd + tab
```

### Crear entorno virtual
```
python -m venv inv
```

### activar entorno virtual
```
inv/Scripts/Activate
```

### Instalar dependencias
```
pip install -r requirements.txt
```

### iniciar el proyecto
```
uvicorn main:app --reload
```
