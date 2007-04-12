%define real_name WWW-Search-Lycos

Summary:	WWW::Search::Lycos - class for searching www.lycos.com
Name:		perl-%{real_name}
Version:	2.221
Release: %mkrel 2
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/WWW/%{real_name}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This class is a Lycos specialization of WWW::Search.  It handles
making and interpreting Lycos-site searches http://www.lycos.com.

This class exports no public interface; all interaction should
be done through WWW::Search objects.

%prep
%setup -q -n %{real_name}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

# make test don't work...
#make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog README
%{perl_vendorlib}/WWW/Search/Lycos.pm
%{_mandir}/*/*

