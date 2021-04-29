package ualbanycsi518.NBATrackr.Final.Services;

import java.util.Base64;

import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpMethod;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;

import ualbanycsi518.NBATrackr.Final.Entities.NBATeamStandings;

@Service
public class NBATeamServiceJpaImpl implements NBATeamService {
    public NBATeamStandings fetchNBATeamStandings() {
        String url = "https://api.mysportsfeeds.com/v1.2/pull/nba/2018-2019-regular/overall_team_standings.json";
		String encoding = Base64.getEncoder().encodeToString("bf73ce8d-01b8-44bf-944c-8e042b:TwVgGi8bANHVnPY".getBytes());

        HttpHeaders headers = new HttpHeaders();
		headers.setContentType(MediaType.APPLICATION_JSON);
		headers.set("Authorization", "Basic " + encoding);
		HttpEntity<String> request = new HttpEntity<String>(headers);

        RestTemplate restTemplate = new RestTemplate();
        ResponseEntity<NBATeamStandings> responseEntity = restTemplate.exchange(url, HttpMethod.GET, request, NBATeamStandings.class);
        NBATeamStandings nbaTeamStandings = responseEntity.getBody();

        return nbaTeamStandings;
    }
}