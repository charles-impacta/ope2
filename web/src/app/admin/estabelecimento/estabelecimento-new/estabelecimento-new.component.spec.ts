import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { EstabelecimentoNewComponent } from './estabelecimento-new.component';

describe('EstabelecimentoNewComponent', () => {
  let component: EstabelecimentoNewComponent;
  let fixture: ComponentFixture<EstabelecimentoNewComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ EstabelecimentoNewComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(EstabelecimentoNewComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
