import { Component } from '@angular/core';
import { AppBaseComponent } from './shared/app-base-component';
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent extends AppBaseComponent {
  title = 'Cardápio na Web';
}
