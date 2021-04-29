package ualbanycsi518.NBATrackr.Final.Controllers;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;

import ualbanycsi518.NBATrackr.Final.Entities.User;
import ualbanycsi518.NBATrackr.Final.Services.UserService;

@Controller
public class UserController {
    @Autowired
    UserService userService;

    @PostMapping("/user-save-favorites")
    public String saveFavorites(@RequestParam(value="favorites", required=false) int[] favoriteTeams, Model model) {
        User user = userService.getCurrentUser();
        user.setFavoriteTeams(favoriteTeams);
        userService.saveUser(user);
        return "redirect:/./user-home";
    }

    @GetMapping("/user-home")
    public String userHome(Model model) {
        User user = userService.getCurrentUser();
        if (user.isBlocked())
            return "redirect:/./logout";
        if (user.isAdmin())
            return "redirect:/./admin-home";
        model.addAttribute("user", user);
        return "UserHomePage";
    }
}
