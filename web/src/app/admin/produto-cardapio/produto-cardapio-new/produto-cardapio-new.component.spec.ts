import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ProdutoCardapioNewComponent } from './produto-cardapio-new.component';

describe('ProdutoCardapioNewComponent', () => {
  let component: ProdutoCardapioNewComponent;
  let fixture: ComponentFixture<ProdutoCardapioNewComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ProdutoCardapioNewComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ProdutoCardapioNewComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
