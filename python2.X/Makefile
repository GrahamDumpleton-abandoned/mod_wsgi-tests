TESTS = $(wildcard *.wsgi)

tests :
	@for file in $(TESTS); \
	do \
	  echo $$file; \
	  python -m doctest $$file; \
	done

clean :
	$(RM) *.pyc
