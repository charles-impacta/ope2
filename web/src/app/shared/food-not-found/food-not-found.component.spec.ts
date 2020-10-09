import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { FoodNotFoundComponent } from './food-not-found.component';

describe('FoodNotFoundComponent', () => {
  let component: FoodNotFoundComponent;
  let fixture: ComponentFixture<FoodNotFoundComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ FoodNotFoundComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(FoodNotFoundComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
