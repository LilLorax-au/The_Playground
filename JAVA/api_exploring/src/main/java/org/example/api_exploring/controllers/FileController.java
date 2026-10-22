package org.example.api_exploring.controllers;

import org.example.api_exploring.handlers.AuthenticateHandler;
import org.springframework.http.HttpStatusCode;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;


@RestController
public class FileController {



    @GetMapping(
            value = "/get-file"
    )
    public @ResponseBody ResponseEntity<String> getFile(
            @RequestParam String file,
            @RequestParam String key
    ){
        if(!AuthenticateHandler.isValid(key)){
            return ResponseEntity
                    .status(HttpStatusCode.valueOf(404))
                    .body("Bad key");
        }
        else {
            return ResponseEntity.ok("Searching for: " + file);
        }
    }


}
