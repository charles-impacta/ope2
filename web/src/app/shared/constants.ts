export class Constants {

  public static hostApi : string = window.location.host.indexOf('localhost') >= 0 ? 'http://localhost:5000' : '/api';

}
