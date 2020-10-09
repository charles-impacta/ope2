import { StatusFlagComponent } from './status-flag/status-flag.component';
import { NavBarComponent } from './nav-bar/nav-bar.component';
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { FoodNotFoundComponent } from './food-not-found/food-not-found.component';

@NgModule({
  imports: [
    CommonModule
  ],
  declarations: [ NavBarComponent,StatusFlagComponent, FoodNotFoundComponent],
  exports: [ NavBarComponent,StatusFlagComponent,FoodNotFoundComponent]
})
export class SharedModule {

}
