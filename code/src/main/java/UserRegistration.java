
import org.picketlink.idm.IdentityManager;
import org.picketlink.idm.credential.Password;

import javax.faces.bean.RequestScoped;
import javax.inject.Inject;
import javax.inject.Named;

@Named
@RequestScoped
public class UserRegistration {

	@Inject
	private IdentityManager identityManager;

	private String loginName;
	private String firstName;
	private String lastName;
	private String password;

	public String register() {
		//identityManager.validateCredentials();
		return "/signin.xhtml";
	}
}