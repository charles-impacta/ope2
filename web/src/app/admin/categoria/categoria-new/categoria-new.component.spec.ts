import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CategoriaNewComponent } from './categoria-new.component';

describe('CategoriaNewComponent', () => {
  let component: CategoriaNewComponent;
  let fixture: ComponentFixture<CategoriaNewComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CategoriaNewComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CategoriaNewComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
