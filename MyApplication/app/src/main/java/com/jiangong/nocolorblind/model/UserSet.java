package com.jiangong.nocolorblind.model;

import java.util.HashMap;
import java.util.Map;

/**
 * Created by jiangong on 11/16/15.
 */
public class UserSet {
    private static Map<String, User> users = new HashMap<String, User>();


    /*
        Method for adding user, return false if username exists
     */
    public boolean addUser(User newUser) {
        String nameTemp = newUser.getUsername();
        if (users.containsKey(nameTemp)) { return false; }
        else {
            users.put(nameTemp, newUser);
        }
        return true;
    }

    /*
        Method for get particular user
     */
    public User getUser(String username) {
        if (!users.containsKey(username)) { return null; }
        return users.get(username);
    }

    /*
        Method for validate user
     */
    public boolean validateUser(User newUser) {
        String nameTemp = newUser.getUsername();
        return (!users.containsKey(nameTemp));
    }


}
