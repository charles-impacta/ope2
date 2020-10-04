import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { EstabelecimentoEditComponent } from './estabelecimento-edit.component';

describe('EstabelecimentoEditComponent', () => {
  let component: EstabelecimentoEditComponent;
  let fixture: ComponentFixture<EstabelecimentoEditComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ EstabelecimentoEditComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(EstabelecimentoEditComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
