package fer.wallezohari.KuhajItAPI;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api")
public class TestHello {

    @GetMapping("/hello")
    public String hello() {
        return "Hello, this is your Spring Boot + PostgreSQL application!";
    }
}