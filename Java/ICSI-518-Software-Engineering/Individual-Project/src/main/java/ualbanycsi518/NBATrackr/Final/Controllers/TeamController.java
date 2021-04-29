package ualbanycsi518.NBATrackr.Final.Controllers;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;

import ualbanycsi518.NBATrackr.Final.Entities.User;
import ualbanycsi518.NBATrackr.Final.Entities.NBATeamStandings;
import ualbanycsi518.NBATrackr.Final.Services.NBATeamService;
import ualbanycsi518.NBATrackr.Final.Services.UserService;

@Controller
public class TeamController {
    @Autowired
    NBATeamService nbaTeamService;

    @Autowired
    UserService userService;
    
    @GetMapping("/team")
    public String showTeamProfile(@RequestParam("id") int teamID, Model model) {
        return "TeamProfilePage";
    }

    @GetMapping("/teams")
    public String listTeams(Model model) {
        User user = userService.getCurrentUser();
        NBATeamStandings nbaTeamStandings = nbaTeamService.fetchNBATeamStandings();
        
        model.addAttribute("user", user);
        model.addAttribute("teamStandings", nbaTeamStandings.getOverallteamstandings().getTeamstandingsentry());
        return "TeamListPage";
    }
}