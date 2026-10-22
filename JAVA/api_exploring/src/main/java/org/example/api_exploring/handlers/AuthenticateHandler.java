package org.example.api_exploring.handlers;

public class AuthenticateHandler {
    private static final String DEF_TEMP_KEY = "test";

    public static boolean isValid(String key){
        // TODO This is to be killed after testing
        key = key.substring(1, key.length() - 1);
        return  key.equals(DEF_TEMP_KEY);
    }
}
