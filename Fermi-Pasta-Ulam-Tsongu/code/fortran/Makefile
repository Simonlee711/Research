FC = gfortran
FFLAGS = -Wall -Wextra -Wimplicit-interface -Wno-surprising -Wno-maybe-uninitialized -fPIC -fmax-errors=1 -g -fcheck=all -fbacktrace

OBJ =  setup_module.o output_module.o leapfrog_module.o fput.o

fput: $(OBJ)
	$(FC) -o $@ $(OBJ) $(FFLAGS)

%.o: %.f90
	$(FC) -c $< $(FFLAGS)

.PHONY: clean

clean:
	rm -f fput *.o *.mod *~
