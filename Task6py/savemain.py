import docker

client = docker.from_env()
container_name = "task6py-web"
image_name = "task6py-web" 

try:
    container = client.containers.get(container_name)
    print(f"Контейнер '{container_name}' уже существует.")
    if container.status != 'running':
        container.start()
        print(f"Контейнер '{container_name}' запущен.")
except docker.errors.NotFound:
    print(f"Контейнер '{container_name}' не найден. Создаем и запускаем...")
    try:
        client.images.get(image_name)
    except docker.errors.ImageNotFound:
        print(f"Образ '{image_name}' не найден. Создайте его или залогиньтесь в Docker Hub.")
    else:
        container = client.containers.run(
            image_name,
            name=container_name,
            detach=True,
            restart_policy={"Name": "always"}
        )
        print(f"Контейнер '{container_name}' создан и запущен.")