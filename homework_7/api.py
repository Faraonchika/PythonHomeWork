import requests
import click
import json


@click.group()
def cli():
    pass

address = "https://cloud-api.yandex.net:443"

headers = {'Authorization': 'OAuth AgAAAAA3aKN5AAX3vFcQtXcFkUx9m2pmqSY-hoE'}


@cli.command()
def show_disk():
    r = requests.get(address + '/v1/disk', headers=headers)
    out = r.json()
    print('Общий объем диска:', out["total_space"])
    print('Используемый объем:', out["used_space"])


@cli.group()
def todo():
    pass


@todo.command()
@click.argument('path')
def get_resources(path):
    params = {"path": path}
    r1 = requests.get(address + '/v1/disk/resources', headers=headers, params=params)
    if r1.status_code == 404:
        print('Такого пути не существует')
    else:
        out = r1.json()
        if out['type'] == 'file':
            print("Имя файла:", out['name'])
            print("Размер в битах:", out[ 'size'])
            print("mime_type:", out['mime_type'])
            print("Был загружен:", out["created"])
        elif out['type'] == "dir":
            dirs = []
            files = []
            for now in out['_embedded']['items']:
                if now['type'] == 'file':
                    files.append(now['name'])
                elif now['type'] == 'dir':
                    dirs.append(now['name'])
            print("Папки:", dirs)
            print("Файлы:", files)


@todo.command()
@click.argument('path')
def download(path):
    params = {"path": path}
    r2 = requests.get(address + '/v1/disk/resources', headers=headers, params=params)
    if r2.status_code == 404:
        print('Такого пути не существует')
    else:
        out = r2.json()
        url = out['file']

        f=open('C:/Users/Рамиль/Desktop' + '/' + out['name'],"wb")
        ufr = requests.get(url)
        f.write(ufr.content)
        f.close()
    if r2.status_code == 202:
        print("Файл успешно загружен")


@todo.command()
@click.argument('path')
def make_folder(path):
    params = {"path": path}
    r2 = requests.put(address + '/v1/disk/resources', headers=headers, params=params)
    if r2.status_code == 202:
        print("Папка успешно создана")


@todo.command()
@click.argument('path')
@click.argument('link')
def upload_post(path, link):
    params = {"url": link, "path": path + '/' + link.split('/')[-1]}
    r = requests.post(address + '/v1/disk/resources/upload', headers=headers, params=params)
    if r.status_code == 202:
        print("Файл успешно загружен")


@todo.command()
@click.argument('path')
@click.argument('url')
def upload_get(path, url):
    try:
        file = open(url, 'rb')
        params = {"path": path + '/' + url.split('\\')[-1]}
        r = requests.get(address + '/v1/disk/resources/upload', headers=headers, params=params)
        if r.status_code == 409:
            print("Файл с таким именем уже существует, либо указана несуществующая директория на диске!")
        else:
            requests.put(r.json()['href'], headers=headers, data=file)
        if r.status_code == 202:
            print("Файл успешно загружен")
    except FileNotFoundError:
        print("Такого файла не существует в заданной директории!")


if __name__ == '__main__':
    cli()
