package ualbanycsi518.NBATrackr.Final.Controllers;

import java.util.List;
import java.util.ArrayList;

import org.springframework.stereotype.Controller;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;

import ualbanycsi518.NBATrackr.Final.Entities.NBATeam;
import ualbanycsi518.NBATrackr.Final.Entities.User;
import ualbanycsi518.NBATrackr.Final.Repositories.NBATeamRepository;
import ualbanycsi518.NBATrackr.Final.Repositories.UserRepository;
import ualbanycsi518.NBATrackr.Final.Services.UserService;

@Controller
public class OldController {

    @Autowired
    private NBATeamRepository teamRepository;

    @Autowired
    private UserRepository userRepository;

    @Autowired
    private UserService userService;
    
    @GetMapping("/old/dummy")
    public String addDummyValues() {
        teamRepository.save(new NBATeam("Washington Wizards", "WAS", "/img/WAS.png"));
		teamRepository.save(new NBATeam("Miami Heat", "MIA", "/img/MIA.png"));
		teamRepository.save(new NBATeam("Los Angeles Clippers", "LAC", "/img/LAC.png"));
        return "redirect:/./old/";
    }

    @GetMapping("/old/")
    public String index(Model model) {
        User user = userService.getCurrentUser();
        model.addAttribute("username", user.getFirstName());
        List<NBATeam> favoriteTeams = new ArrayList<NBATeam>();
        if (user.getFavoriteTeams() != null) {
            for (int favoriteTeam: user.getFavoriteTeams())
                favoriteTeams.add(teamRepository.findById(favoriteTeam));
        }
        model.addAttribute("favoriteTeams", favoriteTeams);    
        return "/old/index";
    }

    @GetMapping("/old/select-favorite-teams")
    public String team(Model model) {
        User user = userService.getCurrentUser();
        model.addAttribute("teams", teamRepository.findAll());
        model.addAttribute("userId", user.getId());
        model.addAttribute("username", user.getFirstName());
        return "/old/select-favorite-teams";
    }

    @PostMapping("/old/select-favorite-teams")
    public String selectTeams(@RequestParam int[] favoriteTeams, @RequestParam int userId) {
        User user = userRepository.findById(userId);
        user.setFavoriteTeams(favoriteTeams);
        userRepository.save(user);
        return "redirect:/./old/";
    }
}