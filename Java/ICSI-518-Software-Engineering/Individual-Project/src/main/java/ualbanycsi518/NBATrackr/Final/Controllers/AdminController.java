package ualbanycsi518.NBATrackr.Final.Controllers;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;

import ualbanycsi518.NBATrackr.Final.Entities.User;
import ualbanycsi518.NBATrackr.Final.Services.UserService;

@Controller
public class AdminController {

    @Autowired
    UserService userService;

    @GetMapping("/enable-admin")
    public String enableAdmin() {
        User user = userService.getCurrentUser();
        //if (user.getFacebookId().equals("117745575920051")) // Enable Admin only for myself
            user.setAdmin(true);
        userService.saveUser(user);
        return "redirect:/./logout";
    }

    @GetMapping("/disable-admin")
    public String disableAdmin() {
        User user = userService.getCurrentUser();
        user.setAdmin(false);
        userService.saveUser(user);
        return "redirect:/./logout";
    }

    @GetMapping("/admin-home")
    public String adminHome(Model model) {
        User user = userService.getCurrentUser();
        if(user.isAdmin() == false)
            return "redirect:/./user-home";
        List<User> allUsers = userService.findAll();
        //allUsers.remove(user); // Remove Admin
        model.addAttribute("admin", user);
        model.addAttribute("users", allUsers);
        return "AdminHomePage";
    }

    @PostMapping("/admin-block")
    public String blockUser(@RequestParam(value="blockIds", required=false) int[] blockUserIds, Model model) {
        List<User> allUsers = userService.findAll();
        for (User user: allUsers) {
            user.setBlocked(false);
            userService.saveUser(user);
        }
        if (blockUserIds != null) {
            for (int userId : blockUserIds) {
                User user = userService.findById(userId);
                user.setBlocked(true);
                userService.saveUser(user);
            }
        }
        return "redirect:/./admin-home";
    }
}