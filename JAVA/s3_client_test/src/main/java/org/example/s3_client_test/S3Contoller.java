package org.example.s3_client_test;

import org.springframework.core.io.Resource;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.Map;

@RestController
public class S3Contoller {


    @GetMapping(path = "s3/bucket")
    public ResponseEntity<Resource> pullFile(){

    }


}
