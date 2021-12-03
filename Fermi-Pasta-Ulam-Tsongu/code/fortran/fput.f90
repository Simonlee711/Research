! File: fput.f90
! Author: Simon Lee
! Purpose: main driver routine which calls the appropriate routines from the remaining files.

program fput
    use leapfrog
    !use output
    use problemsetup, only : N, alpha, runName, problemsetup_Init
    implicit none

    ! get the variables needed for the leapfrog mechanism
    call problemsetup_Init('FPUT.init')

    ! call the leapfrog subroutine
    call leapfrog_mechanism(N, alpha, runName)

end program fput