package com.example.restapi.controller;

import com.example.restapi.model.Item;
import org.springframework.web.bind.annotation.*;

import java.util.ArrayList;
import java.util.List;

@RestController
@RequestMapping("/items")
public class ItemController {

    private List&lt;Item&gt; itemList = new ArrayList&lt;&gt;();

    // GET: получить все элементы
    @GetMapping
    public List&lt;Item&gt; getAllItems() {
        return itemList;
    }

    // POST: добавить новый элемент
    @PostMapping
    public Item addItem(@RequestBody Item item) {
        item.setId((long) (itemList.size() + 1));
        itemList.add(item);
        return item;
    }

    // PUT: обновить элемент по id
    @PutMapping("/{id}")
    public Item updateItem(@PathVariable Long id, @RequestBody Item newItem) {
        for (Item item : itemList) {
            if (item.getId().equals(id)) {
                item.setName(newItem.getName());
                return item;
            }
        }
        return null; // или выбросить исключение
    }

    // DELETE: удалить элемент по id
    @DeleteMapping("/{id}")
    public void deleteItem(@PathVariable Long id) {
        itemList.removeIf(item -&gt; item.getId().equals(id));
    }
}