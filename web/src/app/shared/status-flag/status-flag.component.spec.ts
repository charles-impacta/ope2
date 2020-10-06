import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { StatusFlagComponent } from './status-flag.component';

describe('StatusFlagComponent', () => {
  let component: StatusFlagComponent;
  let fixture: ComponentFixture<StatusFlagComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ StatusFlagComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(StatusFlagComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
