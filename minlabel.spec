Summary:	Creates, views and edits BSD UNIX style disk labels on Alphas
Summary(pl):	Program do tworzenia, przegl±dania i edycji disklabeli BSD UNIX na maszynach Alpha
Name:		minlabel
Version:	1.2
Release:	6
License:	GPL
ExclusiveArch:	alpha
Group:		Base/Utilities
Group(de):	Gründsätzlich/Werkzeuge
Group(pl):	Podstawowe/Narzêdzia
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Alpha machine's hard drives are partitioned in one of two ways: PC
style partitioning or BSD UNIX style labeling. The minlabel program
allows you to create, view and edit BSD UNIX style labels on Alpha
hard drives.

%prep
%setup -q

%build
%{__make} RPM_OPT_FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/sbin

install -m755 minlabel $RPM_BUILD_ROOT/sbin

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
/sbin/minlabel
