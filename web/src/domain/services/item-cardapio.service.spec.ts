import { TestBed } from '@angular/core/testing';

import { ItemCardapioService } from './item-cardapio.service';

describe('ItemCardapioService', () => {
  let service: ItemCardapioService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ItemCardapioService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
