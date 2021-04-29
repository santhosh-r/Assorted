package ualbanycsi518.NBATrackr.Final.Configuration;

// Reference1: https://drissamri.be/blog/java/enable-https-in-spring-boot/
// Reference2: https://stackoverflow.com/questions/47700115/tomcatembeddedservletcontainerfactory-is-missing-in-spring-boot-2

import org.apache.catalina.Context;
import org.apache.catalina.connector.Connector;
import org.apache.tomcat.util.descriptor.web.SecurityCollection;
import org.apache.tomcat.util.descriptor.web.SecurityConstraint;
import org.springframework.boot.web.embedded.tomcat.TomcatServletWebServerFactory;
import org.springframework.boot.web.servlet.server.ServletWebServerFactory;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class ServerConfiguration {
    @Bean
    public ServletWebServerFactory servletContainer() {
        TomcatServletWebServerFactory tomcat = new TomcatServletWebServerFactory() {
            @Override
            protected void postProcessContext(Context context) {
                SecurityConstraint securityConstraint = new SecurityConstraint();
                securityConstraint.setUserConstraint("CONFIDENTIAL");
                SecurityCollection collection = new SecurityCollection();
                collection.addPattern("/*");
                securityConstraint.addCollection(collection);
                context.addConstraint(securityConstraint);
            }
        };

        tomcat.addAdditionalTomcatConnectors(initiateHttpConnector());
        return tomcat;
    }
    
    private Connector initiateHttpConnector() {
      Connector connector = new Connector(TomcatServletWebServerFactory.DEFAULT_PROTOCOL);
      connector.setScheme("http");
      connector.setPort(8080);
      connector.setSecure(false);
      connector.setRedirectPort(8443);
      
      return connector;
    }
}