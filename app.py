import eel, os, shutil

eel.init('web')

@eel.expose
def clean_system(temp_dir):
    try:
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
            os.makedirs(temp_dir, exist_ok=True)
            return "Система очищена (папка очищена)."
        else:
            return "Директория не существует."
    except Exception as e:
        return str(e)

eel.start('initial.html', size=(800,600))