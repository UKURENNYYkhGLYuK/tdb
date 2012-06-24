Summary:	TDB - Trivial Database
Summary(pl):	TDB - prosta baza danych
Name:		tdb
Version:	1.0.6
Release:	3
License:	GPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/tdb/%{name}-%{version}.tar.gz
# Source0-md5:	6b643fdeb48304010dcd5f675e458b58
Patch0:		%{name}-gcc33.patch
Patch1:		%{name}-tdb_store.patch
Patch2:		%{name}-Makefile-extras.patch
URL:		http://sourceforge.net/projects/tdb/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gdbm-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TDB is a Trivial Database. In concept, it is very much like GDBM, and
BSD's DB except that it allows multiple simultaneous writers and uses
locking internally to keep writers from trampling on each other. TDB
is also extremely small.

%description -l pl
TDB to Trivial Database, czyli prosta baza danych. W za�o�eniach jest
bardzo podobna do GDBM lub DB z BSD z wyj�tkiem tego, �e pozwala na
zapis wielu procesom jednocze�nie i u�ywa wewn�trznie blokowania, aby
nie pozwoli� pisz�cym na zadeptanie si� nawzajem. TDB jest ponadto
ekstremalnie ma�a.

%package devel
Summary:	Header files for TDB library
Summary(pl):	Pliki nag��wkowe biblioteki TDB
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for TDB library.

%description devel -l pl
Pliki nag��wkowe biblioteki TDB.

%package static
Summary:	Static TDB library
Summary(pl):	Statyczna biblioteka TDB
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static TDB library.

%description static -l pl
Statyczna biblioteka TDB.

%package extras
Summary:	TDB additional utilities
Summary(pl):	Dodatkowe narz�dzia do TDB
Group:		Applications/Databases
Requires:	%{name} = %{version}-%{release}

%description extras
TDB additional utilities.

%description extras -l pl
Dodatkowe narz�dzia do TDB.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

#install tdbiterate $RPM_BUILD_ROOT%{_bindir}
#install tdbspeed $RPM_BUILD_ROOT%{_bindir}
#install tdbtest $RPM_BUILD_ROOT%{_bindir}
#install tdbtorture $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/tdbdump
%attr(755,root,root) %{_bindir}/tdbtool
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/tdb.h
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files extras
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/tdbiterate
%attr(755,root,root) %{_bindir}/tdbspeed
%attr(755,root,root) %{_bindir}/tdbtest
%attr(755,root,root) %{_bindir}/tdbtorture
