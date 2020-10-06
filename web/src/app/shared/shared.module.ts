import { StatusFlagComponent } from './status-flag/status-flag.component';
import { NavBarComponent } from './nav-bar/nav-bar.component';
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { AppRoutingModule } from '../app-routing.module';

@NgModule({
  imports: [
    CommonModule
  ],
  declarations: [ NavBarComponent,StatusFlagComponent],
  exports: [ NavBarComponent,StatusFlagComponent]
})
export class SharedModule {

}
