


package com.example.demo;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class HelloServiceTest {
    @Test
    void testGetMessage() {
        HelloService helloService = new HelloService();
        assertEquals("Hello", helloService.getMessage());
    }
}


