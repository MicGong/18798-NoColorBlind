package com.jiangong.nocolorblind.model;

/**
 * Created by jiangong on 11/16/15.
 */
public class User {

    private String username;

    /*
     * Color Blind Status:
     * 0 -- Normal
     * 1 -- Abnormal
     */
    private int status;

    /*
        TODO Not sure about the format
     */
    private int[] shift;

    public User (String username) {
        this.username = username;
    }

    /*
        Getters and setters for private field
     */

    public String getUsername() {
        return this.username;
    }

    public void setStatus(int status) {
        this.status = status;
    }

    public int getStatus() {
        return this.status;
    }

}
