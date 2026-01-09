package com.platform.java_service.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.Random;

@RestController
public class PlatformController {

    private final Random random = new Random();

    @GetMapping("/health")
    public String health() {
        return "UP";
    }

    @GetMapping("/process")
    public String process() throws InterruptedException {
        int delay = random.nextInt(2000);
        Thread.sleep(delay);

        if (random.nextInt(10) < 2) {
            throw new RuntimeException("Simulated processing failure");
        }

        return "Processed successfully in " + delay + " ms";
    }

    @GetMapping("/error")
    public String error() {
        throw new RuntimeException("Intentional error triggered");
    }
}
