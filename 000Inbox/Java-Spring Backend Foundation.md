# Java-Spring Backend Foundation

## \[ Main Layer \]

- Controller:  API Endpoints

- **DTO (Data Transfer Object):**  is a **design pattern** used to transfer data between different parts of an application

   - such as **service layer** and the **API response layer**

   - In bus code: **convert `BusEntity` to `BusResDto`** using a mapping function

   ```java
   List<BusResDto> resultList = resultEntities.stream().map(bus -> {
       String operationDate = DateTimeHelper.instantToUtcDateString(bus.getOperationDate());
       String operatorName = ObjectUtils.isEmpty(opMap.get(bus.getOperatorId())) ? "" : opMap.get(bus.getOperatorId()).getName();
       return new BusResDto(
           bus.getPlateNumber(),
           bus.getBusManufacturer(),
           bus.getBusModel(),
           operationDate,
           operatorName
       );
   }).toList();
   ```

- Service: Business Logic

- Repository: Table Operation

- Model: Table/Data Entity



## **\[ JPA- Java ORM (object-relational mapping) \]**

- Jakarta Persistence API (JPA) is a standard for **object-relational mapping (ORM)** in Java. It allows developers to map Java objects to relational database tables and manage their interactions seamlessly.

- What:

   - JPA is a **specification** (standard interface) for ORM in Java ( not a framework )

   - Frameworks like Hibernate, EclipseLink, and others provide implementations of JPA.

   - **Spring Data JPA**  is a library that integrates JPA (and its implementations like Hibernate) with the Spring ecosystem for easier development

- Key Annotations in JPA:

   - 

      ![image 104.png](./Java-Spring%20Backend%20Foundation-assets/image%20104.png)

      

- How - Entity:

   - Create a Java class and annotate it as an **entity**:

   ```java
   import jakarta.persistence.*;
   
   @Entity
   @Table(name = "students") // Optional: Specify table name
   public class Student {
   
       @Id
       @GeneratedValue(strategy = GenerationType.IDENTITY) // Auto-generate ID
       private Long id;
   
       @Column(name = "name", nullable = false) // Map column with constraints
       private String name;
   
       @Column(name = "age")
       private int age;
   
       // Constructors
       public Student() {}
       public Student(String name, int age) {
           this.name = name;
           this.age = age;
       }
   
       // Getters and Setters
       public Long getId() { return id; }
       public String getName() { return name; }
       public void setName(String name) { this.name = name; }
       public int getAge() { return age; }
       public void setAge(int age) { this.age = age; }
   }
   
   ```



- How -  Repository:

   - Create a Repository Interface

   - Use JpaRepository to handle CRUD operations:

```java
import org.springframework.data.jpa.repository.JpaRepository;

public interface StudentRepository extends JpaRepository<Student, Long> {
    // Custom query methods can go here (optional)
}
```



- How - Create a Service Class

   - The `@Autowired` annotation in Spring is used for **automatic dependency injection**. It tells the Spring framework to automatically **inject a bean (a Spring-managed object)** into the class where the annotation is used.

```java
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import java.util.List;

@Service
public class StudentService {

    @Autowired
    private StudentRepository studentRepository;

    public List<Student> getAllStudents() {
        return studentRepository.findAll();
    }

    public Student createStudent(String name, int age) {
        return studentRepository.save(new Student(name, age));
    }
}
```



- How - Create a REST Controller

```java
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/students")
public class StudentController {

    @Autowired
    private StudentService studentService;

    @GetMapping
    public List<Student> getAllStudents() {
        return studentService.getAllStudents();
    }

    @PostMapping
    public Student addStudent(@RequestBody Student student) {
        return studentService.createStudent(student.getName(), student.getAge());
    }
}
```



## \[ **Java DI (**dependency injection**)** \]

- The **`@Autowired`** in Spring is used for **automatic dependency injection**. 

- It tells the Spring framework to automatically **inject a bean (a Spring-managed object)** into the class where the annotation is used.

- What Does @Autowired Do?

   - injects a dependency into a Spring-managed component

   - Spring automatically finds the appropriate bean to inject based on the type of the field, method, or constructor

- How - Field Injection

   - Spring sees the @Autowired annotation on studentRepository.

   - It looks for a bean of type StudentRepository and injects it automatically.

```java
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class StudentService {

    @Autowired  // Automatically injects StudentRepository bean
    private StudentRepository studentRepository;

    public List<Student> getAllStudents() {
        return studentRepository.findAll();
    }
}
```





## \[ bean (a Spring-managed object) \]

- Basic Concept:

   - a bean is an object that is managed, instantiated, and controlled by the Spring IoC (Inversion of Control) container

   - The Spring container is responsible for creating and managing the lifecycle of these beans.

   - Beans are typically components, such as services, repositories, controllers, or other objects, that you want Spring to manage and inject into your application as dependencies.

   - Beans are defined using **annotations** (like `@Component`, `@Service`, `@Repository`, `@Controller`) or XML configuration.

   

- How to Define a Bean - Using Annotations (Recommended) 

   - pring Boot and Spring Framework encourage annotation-based bean configuration.

      - `@Component`: Generic annotation to mark a class as a bean.

      - `@Service`: Specialized for service layer components.

      - `@Repository`: Specialized for data access components.

      - `@Controller`: Specialized for controllers in a web application

   

- How to Define a Bean - Using `@Bean` in a Configuration Class

```java
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration // Indicates this is a configuration class
public class AppConfig {

    @Bean // Explicitly declares a bean
    public StudentService studentService() {
        return new StudentService();
    }
}
```



- Spring IoC Container (Software Level - Java Application)

   - It **not the same** thing to Docker Container

   - Purpose: Manages the lifecycle, creation, and wiring of Java objects (beans) in a Spring application.

   - Scope: Limited to Java applications and specifically to the Spring framework.

   - Nature: It operates within your application process (inside the JVM).

   - Key Role: Dependency injection (DI) and inversion of control (IoC) to simplify Java application development.


