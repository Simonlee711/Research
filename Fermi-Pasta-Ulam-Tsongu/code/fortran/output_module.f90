! File: output_module.f90
! Author: Simon Lee
! Purpose: This writes the solution out to disc as needed

module output
    !use problemsetup
    implicit none
    integer, parameter :: dp = kind(0.d0)
    integer, parameter :: maxFileLen=50, maxStrLen=200
    character(len=maxStrLen), save :: run_name, outFile


contains

    subroutine write_out(xnp1, N, run_name)
        !set loop variable
        implicit none
        integer :: i, N
        logical :: exist
        real (dp), allocatable :: xnp1(:)
        character(len=maxStrLen) :: run_name
        outFile = 'data/' // trim(run_name) // '.Tf.dat'
        inquire(file=outFile, exist=exist)           ! Came from Stack Overflow
        if (exist) then
            open(N, file=outFile, status="old", position="append", action="write")
        else
            open(N, file=outFile, status="new", action="write")
        end if
        
        write(N, *) (xnp1(i),i=1,N)
        close(N)
    
    end subroutine write_out

    subroutine write_out_N(xnp1, N, run_name)
        !set loop variable
        implicit none
        integer :: N
        logical :: exist
        real (dp), allocatable :: xnp1(:)
        character(len=maxStrLen) :: run_name

        outFile = 'data/' // trim(run_name) // '.Ndiv2.dat'
        inquire(file=outFile, exist=exist)           ! Came from Stack Overflow
        if (exist) then
            open(N, file=outFile, status="old", position="append", action="write")
        else
            open(N, file=outFile, status="new", action="write")
        end if
        if (N == 3) then
            write(N, *) (xnp1(N-1))
        else
            write(N, *) (xnp1((N/2)))
        end if 
        close(N)
    end subroutine write_out_N
end module output 