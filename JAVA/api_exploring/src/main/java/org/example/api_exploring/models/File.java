package org.example.api_exploring.models;

public class File {
    private String path;

    private String key;
    private String ext;

    private final String DEF_PATH = "/";
    private final String DEF_KEY = null;
    private final String DEF_EXT = null;

    public File() {
        this.path = DEF_PATH;
        this.key = DEF_KEY;
        this.ext = DEF_EXT;
    }

    public File(String path, String key, String ext){
        this.path = path;
        this.key = key;
        this.ext = ext;
    }

    public String getPath() {
        return path;
    }

    public String getKey() {
        return key;
    }

    public String getExt() {
        return ext;
    }

    public void setPath(String path) {
        this.path = path;
    }

    public void setKey(String key) {
        this.key = key;
    }

    public void setExt(String ext) {
        this.ext = ext;
    }
}
