Summary:	Creates, views and edits BSD UNIX style disk labels on Alphas
Summary(pl):	Program do tworzenia, przegl±dania i edycji disklabeli BSD UNIX na maszynach Alpha
Name:		minlabel
Version:	1.2
Release:	6
License:	GPL
Group:		Base/Utilities
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:  6e68adf093485f7a058b0c209e5e93c5
ExclusiveArch:	alpha
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Alpha machine's hard drives are partitioned in one of two ways: PC
style partitioning or BSD UNIX style labeling. The minlabel program
allows you to create, view and edit BSD UNIX style labels on Alpha
hard drives.

%description -l pl
Dyski twarde w maszynach Alpha s± partycjonowane na dwa sposoby: na
partycje w stylu PC lub labele w stylu BSD UNIX. Program minlabel
pozwala tworzyæ, ogl±daæ i modyfikowaæ labele w stylu BSD UNIX na
dyskach twardych maszyn Alpha.

%prep
%setup -q

%build
%{__make} RPM_OPT_FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/sbin

install minlabel $RPM_BUILD_ROOT/sbin

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) /sbin/minlabel
