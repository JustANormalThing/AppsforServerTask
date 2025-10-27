package com.example.restapi;

public class Item {
    private Long id;
    private String name;
    private int age;
    
    public Item() {}
    public Item(Long id, String name,int age ) {
        this.id = id;
        this.name = name;
        this.age = age;
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getage(){
        return age; 
    }

    public void setage(int age) {
         this.age = age;
    }
}