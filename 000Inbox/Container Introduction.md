---
tags:
  - container
---
# Container Introduction

- There are two main steps to run an application as a container:

   1. **Package the app as an *image***

   2. **Run it as a *container***

![CleanShot 2024-12-05 at 23.51.37@2x.png](./Container%20Introduction-assets/CleanShot%202024-12-05%20at%2023.51.37@2x.png)



## \[ Container Introduction \]

- a container is an *isolated execution environment*

- Container 像是資源使用上更彈性的 VM

![CleanShot 2024-12-05 at 23.04.54@2x.png](./Container%20Introduction-assets/CleanShot%202024-12-05%20at%2023.04.54@2x.png)

- Containers vs Virtual Machines

   - both are ways of *packaging* applications and are both forms of *virtualisation*

   - On the virtualisation front, 

      - VMs virtualise hardware

      -  containers virtualise operating systems (OS)

   - For example:

      - **Every VM looks, smells, and feels exactly like a physical server**

      - **Every container looks, smells, and feels exactly like a regular OS**

![image 105.png](./Container%20Introduction-assets/image%20105.png)



- Container just like a object,  image just like a class

   - a class can be instantiated to a lot of object

![CleanShot 2025-01-19 at 08.24.38@2x.png](./Container%20Introduction-assets/CleanShot%202025-01-19%20at%2008.24.38@2x.png)





## \[ Images Introduction\]

![image 106.png](./Container%20Introduction-assets/image%20106.png)



![image 107.png](./Container%20Introduction-assets/image%20107.png)

### What

- Image 就是一堆檔案，根據 Docker File 把一堆檔案安排放置好

   - **image** is a collection of read-only layers. 

   - Each **layer** represents a set of file system changes relative to the layer below it. 

   - All layers are stacked on top of each other, creating a unified view of the file system when a container is run

### What does Layer Mean?

- Each layer are read-only files that represent instructions in the Dockerfile. 

- Each layer contains the **difference** from the previous layer.

- Docker uses a **union file system** to manage these layers efficiently.

- Each **layer** corresponds to 

   - a **directory** in the **Docker storage driver** 

   - Inside these directories, Docker stores **files and metadata** that represent changes made by each layer.

- Example:

```bash
FROM ubuntu:latest  # Layer 1: Base image
COPY myapp /app     # Layer 2: Copies files
RUN apt-get update  # Layer 3: Runs a command
RUN apt-get install -y curl  # Layer 4: Installs curl
```



- Base Images: 

   - Most Docker images are built on top of a "base image." This base image provides the foundation for the file system and includes essential components like:   

      - A minimal Linux distribution (e.g., Alpine Linux, Debian, Ubuntu). These distributions are often stripped down to reduce their size. 

      - Core libraries and utilities needed to run applications.

      - Don't include  full operating system like  physical/virtual  machine.



## \[ Docker File \]

- The most common way to build an image is with a *Dockerfile* and the `docker build` command.

- The Dockerfile is a list of instructions that tell `docker build` how to build the image.

- think of images and containers as similar to:   class and objects

- Example: below fourth line is metadata telling Docker how to start the app

![CleanShot 2025-01-19 at 08.18.39@2x.png](./Container%20Introduction-assets/CleanShot%202025-01-19%20at%2008.18.39@2x.png)

- `docker build -t my-image . -f Dockerfile`

   - Build Process

      - Download the base os

      - Copy in the app and list of dependencies 

      - Install dependencies

      - Record the command to run the app

![CleanShot 2025-01-19 at 08.23.19@2x.png](./Container%20Introduction-assets/CleanShot%202025-01-19%20at%2008.23.19@2x.png)









## \[ What is Docker \]

- Docker is an **open-source platform** ( a lot of code )

- Docker allows you to develop, ship, and run applications inside containers. 

- Docker provides a **complete ecosystem** for containerized applications, handling everything from image creation to orchestration.

- Docker can handle most of the **development-to-deployment flow**, but for production, it usually works **with other tools** like Kubernetes for large-scale orchestration.

![CleanShot 2025-01-19 at 08.36.05@2x.png](./Container%20Introduction-assets/CleanShot%202025-01-19%20at%2008.36.05@2x.png)





# \[ Note \]

- The ++[Open Container Initiative (OCI)](https://opencontainers.org/)++ is a governance body responsible for developing and maintaining the core standards that have enabled the container ecosystem to thrive. It currently maintains three specifications:

   - **Image spec:** defines standards around image format, such as structure, contents, and metadata

   - **Runtime spec:** defines how images should be unpacked and executed as containers

   - **Distribution spec:** standardises the distribution of container images via registries

   

- It’s also common to run containers on top of virtual machines. Most setups like this run multiple containers per VM. Figure 1.8 shows two VMs on the same host, each running multiple containers.

![image 108.png](./Container%20Introduction-assets/image%20108.png)

- Windows hosts with *WSL 2* installed. WSL 2 is the *Windows Subsystem for Linux* and provides a Linux kernel on Windows hosts.


